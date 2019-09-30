import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PromocionComponentComponent } from './promocion-component.component';

describe('PromocionComponentComponent', () => {
  let component: PromocionComponentComponent;
  let fixture: ComponentFixture<PromocionComponentComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PromocionComponentComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PromocionComponentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
